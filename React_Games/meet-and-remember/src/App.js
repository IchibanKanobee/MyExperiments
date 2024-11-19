import React, { useState, useEffect } from "react";
import "./App.css";

// Sample character data
const charactersData = [
  {
    name: "Alice",
    profession: "Teacher",
    funFact: "Loves hiking",
    pet: "Dog",
    birthday: "March 10",
  },
  {
    name: "Bob",
    profession: "Engineer",
    funFact: "Plays guitar",
    pet: "Parrot",
    birthday: "June 15",
  },
  {
    name: "Carol",
    profession: "Doctor",
    funFact: "Has a pet cat",
    pet: "Cat",
    birthday: "July 22",
  },
  {
    name: "David",
    profession: "Chef",
    funFact: "Enjoys cooking Italian food",
    pet: "Fish",
    birthday: "January 5",
  },
];

function App() {
  const [level, setLevel] = useState(1);
  const [characters, setCharacters] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [showQuiz, setShowQuiz] = useState(false);
  const [userAnswer, setUserAnswer] = useState("");
  const [feedback, setFeedback] = useState("");
  const [score, setScore] = useState(0);

  // Set characters based on level
  useEffect(() => {
    setCharacters(charactersData.slice(0, level + 2)); // Adjust the number of characters based on the level
    setCurrentIndex(0);
    setShowQuiz(false);
    setUserAnswer("");
    setFeedback("");
    setScore(0);
  }, [level]);

  // Handle character introduction phase
  const handleNextCharacter = () => {
    if (currentIndex < characters.length - 1) {
      setCurrentIndex(currentIndex + 1);
    } else {
      setShowQuiz(true);
    }
  };

  // Handle quiz answer
  const handleAnswer = () => {
    if (
      userAnswer.toLowerCase() === characters[currentIndex].name.toLowerCase()
    ) {
      setFeedback("Correct!");
      setScore(score + 1);
    } else {
      setFeedback(
        `Incorrect! The correct answer is ${characters[currentIndex].name}.`
      );
    }
    setUserAnswer(""); // Reset answer for next question
  };

  // Check if character data is available
  const currentCharacter = characters[currentIndex];

  return (
    <div className="App">
      <h1>Meet & Remember!</h1>
      {showQuiz ? (
        <div>
          <h2>Quiz Time!</h2>
          {currentCharacter && (
            <>
              <h3>{currentCharacter.profession}</h3>
              <p>What is their name?</p>
              <input
                type="text"
                value={userAnswer}
                onChange={(e) => setUserAnswer(e.target.value)}
              />
              <button onClick={handleAnswer}>Submit Answer</button>
              <p>{feedback}</p>
            </>
          )}
          <button
            onClick={() => {
              if (currentIndex < characters.length - 1) {
                setCurrentIndex(currentIndex + 1);
                setFeedback("");
              } else {
                setShowQuiz(false); // Reset quiz phase
                setLevel((prevLevel) => prevLevel + 1); // Increase level
              }
            }}
          >
            Next
          </button>
        </div>
      ) : (
        <div>
          <h2>Meet the Characters</h2>
          {currentCharacter && (
            <>
              <h3>{currentCharacter.name}</h3>
              <p>Profession: {currentCharacter.profession}</p>
              <p>Fun Fact: {currentCharacter.funFact}</p>
              <p>Pet: {currentCharacter.pet}</p>
              <p>Birthday: {currentCharacter.birthday}</p>
              <button onClick={handleNextCharacter}>Next Character</button>
              {currentIndex === characters.length - 1 && (
                <button onClick={() => setShowQuiz(true)}>Start Quiz</button>
              )}
            </>
          )}
        </div>
      )}
      <p>Score: {score}</p>
      <p>Current Level: {level}</p>
    </div>
  );
}

export default App;
