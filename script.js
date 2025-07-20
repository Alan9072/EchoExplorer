document.addEventListener('DOMContentLoaded', () => {
    const gridArea = document.getElementById('grid-area');
    const instructionElement = document.getElementById('instruction');
    const resetButton = document.getElementById('reset-button');

    const sounds = {
        dog: document.getElementById('sound-dog'),
        cat: document.getElementById('sound-cat'),
        peacock: document.getElementById('sound-peacock'),
        bell: document.getElementById('sound-bell'),
        water: document.getElementById('sound-water'),
        car: document.getElementById('sound-car'),
        correct: document.getElementById('sound-correct'),
        incorrect: document.getElementById('sound-incorrect')
    };

    const soundNames = ['dog', 'cat', 'peacock', 'bell', 'water', 'car'];
    let currentTargetSound = '';
    let utterance = null;
    let currentPreviewSound = null;

    // Define the 6 possible grid positions (row, column)
    const gridPositions = [
        { row: 1, col: 1 }, { row: 1, col: 2 }, { row: 1, col: 3 },
        { row: 2, col: 1 }, { row: 2, col: 2 }, { row: 2, col: 3 }
    ];

    // --- Helper Functions (unchanged) ---
    function speak(text, callback = () => {}) {
        if ('speechSynthesis' in window) {
            if (utterance) {
                window.speechSynthesis.cancel();
            }
            utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'en-US';
            utterance.onend = callback;
            window.speechSynthesis.speak(utterance);
        } else {
            console.warn("Speech Synthesis not supported in this browser.");
            callback();
        }
    }

    function playSound(soundId) {
        if (currentPreviewSound && !currentPreviewSound.paused) {
            currentPreviewSound.pause();
            currentPreviewSound.currentTime = 0;
        }

        const sound = sounds[soundId];
        if (sound) {
            sound.currentTime = 0;
            sound.play().catch(e => console.error(`Error playing sound ${soundId}:`, e));
            return sound;
        }
        return null;
    }

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
        return array;
    }

    // --- Game Logic Functions ---

    function startGame() {
        if (utterance) window.speechSynthesis.cancel();
        if (currentPreviewSound && !currentPreviewSound.paused) {
            currentPreviewSound.pause();
            currentPreviewSound.currentTime = 0;
            currentPreviewSound = null;
        }

        gridArea.innerHTML = ''; // Clear all existing buttons

        // Shuffle both sound names and grid positions
        const shuffledSoundNames = shuffleArray([...soundNames]);
        const shuffledGridPositions = shuffleArray([...gridPositions]);

        // Pair each sound with a random grid position
        const soundGridPairs = shuffledSoundNames.map((soundName, idx) => ({
            soundName,
            position: shuffledGridPositions[idx]
        }));

        soundGridPairs.forEach(({ soundName, position }) => {
            const button = document.createElement('button');
            button.classList.add('sound-spot');
            button.dataset.sound = soundName;
            button.setAttribute('aria-label', `Sound spot. Plays ${soundName} sound on hover or focus.`);

            // Assign the random grid position to this button's style
            button.style.gridRow = position.row;
            button.style.gridColumn = position.col;

            // Add all event listeners
            button.addEventListener('mouseover', () => {
                currentPreviewSound = playSound(soundName);
            });

            button.addEventListener('mouseout', () => {
                if (currentPreviewSound && !currentPreviewSound.paused) {
                    currentPreviewSound.pause();
                    currentPreviewSound.currentTime = 0;
                    currentPreviewSound = null;
                }
            });

            button.addEventListener('focus', () => {
                currentPreviewSound = playSound(soundName);
            });

            button.addEventListener('blur', () => {
                if (currentPreviewSound && !currentPreviewSound.paused) {
                    currentPreviewSound.pause();
                    currentPreviewSound.currentTime = 0;
                    currentPreviewSound = null;
                }
            });

            button.addEventListener('click', () => {
                if (currentPreviewSound && !currentPreviewSound.paused) {
                    currentPreviewSound.pause();
                    currentPreviewSound.currentTime = 0;
                    currentPreviewSound = null;
                }

                if (soundName === currentTargetSound) {
                    playSound('correct');
                    speak(`You found the ${soundName}! Great job!`, () => {
                        setTimeout(() => {
                            button.blur();
                            startGame(); // Randomize grid and pick new target
                        }, 1500);
                    });
                } else {
                    playSound('incorrect');
                    speak(`That's not the ${currentTargetSound}. Try again.`, () => {
                        button.blur();
                        startGame(); // Randomize grid and pick new target
                    });
                }
            });

            gridArea.appendChild(button);
        });

        pickNewTarget();
    }

    function pickNewTarget() {
        const randomIndex = Math.floor(Math.random() * soundNames.length);
        currentTargetSound = soundNames[randomIndex];
        instructionElement.textContent = `Find the ${currentTargetSound}!`;
        speak(`Find the ${currentTargetSound}!`);
    }

    resetButton.addEventListener('click', startGame);
    
    startGame();
});