import React, { useState, useEffect } from "react";
import "./App.css";

// Generate a random Sudoku puzzle based on difficulty level
const generateSudoku = (difficulty) => {
  const basePuzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
  ];

  const clues = Math.max(17, 81 - difficulty * 2);
  let puzzle = JSON.parse(JSON.stringify(basePuzzle));

  for (let i = 0; i < 81 - clues; i++) {
    let x = Math.floor(Math.random() * 9);
    let y = Math.floor(Math.random() * 9);
    if (puzzle[x][y] !== 0) {
      puzzle[x][y] = 0;
    } else {
      i--;
    }
  }
  return puzzle;
};

const checkSolution = (puzzle) => {
  const isValidRow = (row) => {
    const nums = row.filter((n) => n !== 0);
    return new Set(nums).size === nums.length;
  };

  const isValidColumn = (puzzle, colIndex) => {
    const nums = puzzle.map((row) => row[colIndex]).filter((n) => n !== 0);
    return new Set(nums).size === nums.length;
  };

  const isValidBox = (puzzle, rowIndex, colIndex) => {
    const boxNums = [];
    const boxRowStart = Math.floor(rowIndex / 3) * 3;
    const boxColStart = Math.floor(colIndex / 3) * 3;

    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        const num = puzzle[boxRowStart + i][boxColStart + j];
        if (num !== 0) boxNums.push(num);
      }
    }
    return new Set(boxNums).size === boxNums.length;
  };

  for (let i = 0; i < 9; i++) {
    if (!isValidRow(puzzle[i]) || !isValidColumn(puzzle, i)) return false;
  }

  for (let i = 0; i < 9; i += 3) {
    for (let j = 0; j < 9; j += 3) {
      if (!isValidBox(puzzle, i, j)) return false;
    }
  }

  return true;
};

function App() {
  const [difficulty, setDifficulty] = useState(1);
  const [puzzle, setPuzzle] = useState(generateSudoku(difficulty));
  const [playerInput, setPlayerInput] = useState(
    JSON.parse(JSON.stringify(puzzle))
  );
  const [isSolved, setIsSolved] = useState(false);

  useEffect(() => {
    setPuzzle(generateSudoku(difficulty));
    setPlayerInput(JSON.parse(JSON.stringify(puzzle)));
  }, [difficulty]);

  const handleInputChange = (row, col, value) => {
    const updatedPuzzle = [...playerInput];
    updatedPuzzle[row][col] = value === "" ? 0 : parseInt(value);
    setPlayerInput(updatedPuzzle);
  };

  const handleCheckSolution = () => {
    setIsSolved(checkSolution(playerInput));
  };

  return (
    <div className="App">
      <h1>Sudoku Game</h1>

      <div className="sudoku-container">
        <div className="sudoku-grid">
          {puzzle.map((row, rowIndex) => (
            <div className="sudoku-row" key={rowIndex}>
              {row.map((cell, colIndex) => (
                <input
                  type="text"
                  className="sudoku-cell"
                  key={colIndex}
                  value={
                    playerInput[rowIndex][colIndex] === 0
                      ? ""
                      : playerInput[rowIndex][colIndex]
                  }
                  onChange={(e) =>
                    handleInputChange(rowIndex, colIndex, e.target.value)
                  }
                  maxLength="1"
                  disabled={puzzle[rowIndex][colIndex] !== 0} // Disable editing original numbers
                />
              ))}
            </div>
          ))}
        </div>

        {/* Difficulty Slider and Button positioned below */}
        <div className="controls">
          <label>
            Difficulty: {difficulty}
            <input
              type="range"
              min="1"
              max="100"
              value={difficulty}
              onChange={(e) => setDifficulty(parseInt(e.target.value))}
            />
          </label>
          <button onClick={handleCheckSolution}>Check Solution</button>
        </div>

        {isSolved && (
          <p className="success-message">
            Congratulations! You've solved the puzzle!
          </p>
        )}
      </div>
    </div>
  );
}

export default App;
