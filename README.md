# Echo Explorer: An Inclusive Sound Game

## Overview
Echo Explorer is a web-based game designed for children with visual impairment. It provides an engaging and accessible experience where players rely entirely on auditory cues and spoken instructions to interact and succeed. The game's core principle is "auditory primacy," ensuring equal play for children who cannot rely on visual information.

## Live Demo
[YOUR_VERCEL_OR_NETLIFY_LINK_HERE]

## How to Play
1.  The game will speak an instruction, asking you to "Find the [sound name]!" (e.g., "Find the dog!").
2.  Click or tap on the large, invisible buttons on the screen. Each button plays a unique sound.
3.  Listen carefully to the sounds.
4.  When you click the button that plays the target sound, you'll receive positive auditory and spoken feedback, and a new target will be given.

## Accessibility Features
* **Auditory-First Design:** All essential game information, instructions, and feedback are conveyed through sounds and text-to-speech (Web Speech API).
* **Minimal Visual Reliance:** The game is fully playable by children who are blind or have low vision. Visuals are minimal and high-contrast, serving only as optional enhancements.
* **Simple Interaction:** Large, easy-to-target clickable areas (buttons) reduce the need for fine motor skills.
* **Keyboard Navigable:** Users can tab through elements, with screen readers announcing the purpose of each sound spot (via `aria-label`).
* **Positive Reinforcement:** Focus on success and learning without punitive "game over" states or time pressure.
* **ARIA Attributes:** Strategic use of `aria-live="polite"` for dynamic instruction updates and `aria-label` for screen reader clarity on buttons.

## Technologies Used
* HTML5
* CSS3
* Vanilla JavaScript
* Web Speech API (for text-to-speech)
* HTML Audio Elements (for playing sound effects)

## Local Setup
To run this project locally:
1.  Clone the repository: `git clone [YOUR_REPO_URL]`
2.  Navigate to the project directory: `cd echo-explorer`
3.  Open `index.html` in your web browser. Ensure you have the `assets` folder with the `.mp3` files.

## Project Structure