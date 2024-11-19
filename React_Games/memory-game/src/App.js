import React, { useState, useEffect } from "react";
import Card from "./Card";
import "./App.css";

const initialCards = [
  { id: 1, img: "🍎", matched: false },
  { id: 2, img: "🍌", matched: false },
  { id: 3, img: "🍓", matched: false },
  { id: 4, img: "🍇", matched: false },
  { id: 5, img: "🍉", matched: false },
  { id: 6, img: "🍍", matched: false },
  { id: 7, img: "🍋", matched: false },
  { id: 8, img: "🍒", matched: false },
];

function App() {
  const [cards, setCards] = useState([]);
  const [flippedCards, setFlippedCards] = useState([]);
  const [moves, setMoves] = useState(0);
  const [matchedPairs, setMatchedPairs] = useState(0);
  const [disabled, setDisabled] = useState(false);

  // Shuffle and duplicate the cards
  useEffect(() => {
    const shuffledCards = shuffleCards([...initialCards, ...initialCards]);
    setCards(shuffledCards);
  }, []);

  const shuffleCards = (cardsArray) => {
    return cardsArray.sort(() => Math.random() - 0.5);
  };

  const handleCardClick = (index) => {
    if (disabled) return;

    const clickedCard = cards[index];
    const alreadyFlipped =
      flippedCards.findIndex((card) => card.index === index) !== -1;

    if (!alreadyFlipped && flippedCards.length < 2) {
      setFlippedCards([...flippedCards, { ...clickedCard, index }]);

      if (flippedCards.length === 1) {
        checkForMatch(clickedCard, flippedCards[0]);
      }
    }
  };

  const checkForMatch = (card1, card2) => {
    setDisabled(true);

    if (card1.img === card2.img) {
      const updatedCards = cards.map((card) => {
        if (card.img === card1.img) {
          return { ...card, matched: true };
        }
        return card;
      });
      setCards(updatedCards);
      setMatchedPairs(matchedPairs + 1);
    }

    setTimeout(() => {
      setFlippedCards([]);
      setMoves(moves + 1);
      setDisabled(false);
    }, 1000);
  };

  const resetGame = () => {
    const shuffledCards = shuffleCards([...initialCards, ...initialCards]);
    setCards(shuffledCards);
    setFlippedCards([]);
    setMoves(0);
    setMatchedPairs(0);
    setDisabled(false);
  };

  return (
    <div className="App">
      <h1>Memory Match Game</h1>
      <p>Moves: {moves}</p>
      <div className="cards-grid">
        {cards.map((card, index) => (
          <Card
            key={index}
            card={card}
            index={index}
            onClick={handleCardClick}
            isFlipped={
              flippedCards.find((c) => c.index === index) || card.matched
            }
          />
        ))}
      </div>
      {matchedPairs === initialCards.length && (
        <div>
          <h2>Congratulations! You matched all pairs!</h2>
          <button onClick={resetGame}>Play Again</button>
        </div>
      )}
    </div>
  );
}

export default App;
