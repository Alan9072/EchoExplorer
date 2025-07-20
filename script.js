document.addEventListener('DOMContentLoaded', () => {
    const gridArea = document.getElementById('grid-area');
    const instructionElement = document.getElementById('instruction');
    const resetButton = document.getElementById('reset-button');

    const sounds = {
        dog: document.getElementById('sound-dog'),
        cat: document.getElementById('sound-cat'),
        bird: document.getElementById('sound-bird'),
        bell: document.getElementById('sound-bell'),
        water: document.getElementById('sound-water'),
        car: document.getElementById('sound-car'),
        correct: document.getElementById('sound-correct'),
        incorrect: document.getElementById('sound-incorrect')
    };

    const soundNames = ['dog', 'cat', 'bird', 'bell', 'water', 'car'];
    let currentTargetSound = '';
    let utterance = null;
    let currentPreviewSound = null;
    let gameStarted = false;
    let buttonsEnabled = false;

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

        // Reset button appearance
        resetButton.textContent = "New Game";
        resetButton.style.backgroundColor = "#007bff"; // Back to blue

        // Disable buttons until question is finished
        buttonsEnabled = false;

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
            
            // Initially disable buttons with visual feedback
            button.style.opacity = '0.3';
            button.style.pointerEvents = 'none';

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
                // Don't allow clicking until the question is finished
                if (!buttonsEnabled) return;

                if (currentPreviewSound && !currentPreviewSound.paused) {
                    currentPreviewSound.pause();
                    currentPreviewSound.currentTime = 0;
                    currentPreviewSound = null;
                }

                if (soundName === currentTargetSound) {
                    // Immediately disable all buttons to prevent further clicking
                    buttonsEnabled = false;
                    const allButtons = gridArea.querySelectorAll('.sound-spot');
                    allButtons.forEach(btn => {
                        btn.style.pointerEvents = 'none';
                        btn.style.opacity = '0.5';
                    });

                    // Show congratulations text immediately
                    instructionElement.textContent = "Congratulations! You found it!";

                    playSound('correct');
                    speak(`You found the ${soundName}! Great job!`, () => {
                        button.blur();
                        showRestartOption();
                    });
                } else {
                    playSound('incorrect');
                    speak(`That's not the ${currentTargetSound}. Try again.`, () => {
                        button.blur();
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
        if (gameStarted) {
            speak(`Find the ${currentTargetSound}!`, () => {
                // Enable buttons after speech is finished
                enableButtons();
            });
        } else {
            // If game hasn't started yet, enable buttons immediately
            enableButtons();
        }
    }

    function enableButtons() {
        buttonsEnabled = true;
        const allButtons = gridArea.querySelectorAll('.sound-spot');
        allButtons.forEach(btn => {
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
        });
    }

    function showRestartOption() {
        // Buttons are already disabled from the click handler
        // Update instruction for next round and button
        instructionElement.textContent = "Great job! Click 'Next Round' or press any key to continue.";
        resetButton.textContent = "Next Round";
        resetButton.style.backgroundColor = "#007bff"; // Blue color for next round
    }

    function initializeAudioContext() {
        // This function enables audio and speech synthesis after user interaction
        gameStarted = true;
        instructionElement.textContent = "Game starting...";
        
        // Try to initialize speech synthesis
        if ('speechSynthesis' in window) {
            // Create a brief test utterance to enable speech synthesis
            const testUtterance = new SpeechSynthesisUtterance('');
            window.speechSynthesis.speak(testUtterance);
            window.speechSynthesis.cancel();
        }
        
        // Start the game after a brief delay
        setTimeout(() => {
            startGame();
        }, 100);
    }

    resetButton.addEventListener('click', () => {
        if (!gameStarted) {
            initializeAudioContext();
            resetButton.textContent = "New Game";
        } else {
            startGame();
        }
    });

    // Add keyboard support - press any key to start or continue
    document.addEventListener('keydown', (event) => {
        // Prevent default behavior for space/enter to avoid double-triggering
        if (event.code === 'Space' || event.code === 'Enter') {
            event.preventDefault();
        }
        
        if (!gameStarted) {
            // Start the game
            initializeAudioContext();
            resetButton.textContent = "New Game";
        } else if (resetButton.textContent === "Next Round") {
            // Continue to next round
            startGame();
        }
    });
    
    // Wait for speech synthesis to be ready before starting
    function initializeGame() {
        instructionElement.textContent = "Click 'Start Game' or press any key to begin!";
        resetButton.textContent = "Start Game";
    }
    
    initializeGame();
});