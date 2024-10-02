import React, { useState, useEffect } from "react";
import "./App.css";

// Use Unicode fruit symbols for the memory cards
// Extended fruit symbols to 20
const fruitSymbols = [
  "🍎",
  "🍌",
  "🍊",
  "🍓",
  "🍉",
  "🍇",
  "🍒",
  "🍍",
  "🥭",
  "🍑",
  "🍈",
  "🍋",
  "🍏",
  "🥝",
  "🍐",
  "🍅",
  "🥥",
  "🍆",
  "🍠",
  "🍒",
];

// Function to shuffle the cards
const shuffleArray = (array) => {
  return array
    .concat(array) // duplicate the images to get pairs
    .sort(() => Math.random() - 0.5); // shuffle
};

// Function to calculate the best row and column configuration
function calculateGridDimensions(numPairs) {
  const totalCards = numPairs * 2;
  let bestRows = 1;
  let bestCols = totalCards;

  // Try to find two factors of totalCards that are as close as possible
  for (let rows = 1; rows <= Math.sqrt(totalCards); rows++) {
    if (totalCards % rows === 0) {
      const cols = totalCards / rows;
      if (Math.abs(rows - cols) < Math.abs(bestRows - bestCols)) {
        bestRows = rows;
        bestCols = cols;
      }
    }
  }
  return { rows: bestRows, cols: bestCols };
}

function App() {
  const [numFruits, setNumFruits] = useState(4); // Default number of fruits
  const [cards, setCards] = useState(
    shuffleArray(fruitSymbols.slice(0, numFruits))
  );
  const [flippedCards, setFlippedCards] = useState([]);
  const [matchedCards, setMatchedCards] = useState([]);
  const [clickCount, setClickCount] = useState(0);
  const [timer, setTimer] = useState(10); // Start timer at 10 seconds
  const [gameStarted, setGameStarted] = useState(false);
  const [rows, setRows] = useState(2);
  const [cols, setCols] = useState(2);

  // Re-shuffle cards when number of fruits changes
  useEffect(() => {
    setCards(shuffleArray(fruitSymbols.slice(0, numFruits)));
    setFlippedCards([]);
    setMatchedCards([]);
    setClickCount(0);
    setTimer(10);
    setGameStarted(false);

    // Calculate the grid dimensions
    const { rows, cols } = calculateGridDimensions(numFruits);
    setRows(rows);
    setCols(cols);
  }, [numFruits]);

  // Start the timer countdown
  useEffect(() => {
    if (timer > 0 && !gameStarted) {
      const countdown = setTimeout(() => {
        setTimer(timer - 1);
      }, 1000);
      return () => clearTimeout(countdown);
    } else if (timer === 0) {
      // Flip all cards to question marks when timer reaches 0
      setFlippedCards([]);
      setGameStarted(true);
    }
  }, [timer, gameStarted]);

  // Handle card click
  const handleCardClick = (index) => {
    if (
      flippedCards.length === 2 ||
      matchedCards.includes(index) ||
      flippedCards.includes(index)
    )
      return;

    setClickCount(clickCount + 1); // Increment click count
    setFlippedCards([...flippedCards, index]); // Add clicked card to flipped cards

    if (flippedCards.length === 1) {
      // Check if the two flipped cards match
      const firstIndex = flippedCards[0];
      const secondIndex = index;
      if (cards[firstIndex] === cards[secondIndex]) {
        setMatchedCards([...matchedCards, firstIndex, secondIndex]);
      }

      // Reset flipped cards after 1 second
      setTimeout(() => {
        setFlippedCards([]);
      }, 1000);
    }
  };

  // Handle change in number of fruits
  const handleNumFruitsChange = (event) => {
    setNumFruits(parseInt(event.target.value));
  };

  // Force the grid to be a square based on the number of fruits
  const gridSize = numFruits * 2;

  return (
    <div className="App">
      <h1>Memory Card Game</h1>

      {/* Control for number of fruits */}
      <label htmlFor="numFruits">Number of Fruits: </label>
      <select id="numFruits" value={numFruits} onChange={handleNumFruitsChange}>
        {[...Array(fruitSymbols.length - 1).keys()].map((i) => (
          <option key={i + 2} value={i + 2}>
            {i + 2}
          </option>
        ))}
      </select>

      <p>Clicks: {clickCount}</p>

      {/* Timer display */}
      {!gameStarted && <p>Memory Phase: {timer}s remaining</p>}

      {/* Card grid */}
      <div
        className="grid"
        style={{
          gridTemplateColumns: `repeat(${cols}, 100px)`,
          gridTemplateRows: `repeat(${rows}, 100px)`,
        }}
      >
        {cards.map((fruit, index) => (
          <div
            key={index}
            className={`card ${
              flippedCards.includes(index) || matchedCards.includes(index)
                ? "flipped"
                : ""
            }`}
            onClick={() => handleCardClick(index)}
          >
            {flippedCards.includes(index) ||
            matchedCards.includes(index) ||
            !gameStarted ? (
              <span className="fruit-symbol">{fruit}</span>
            ) : (
              <div className="question-mark">?</div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
