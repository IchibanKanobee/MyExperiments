import React from "react";
import "./Card.css";

const Card = ({ card, onClick, isFlipped, index }) => {
  const handleClick = () => {
    if (!isFlipped) {
      onClick(index);
    }
  };

  return (
    <div className={`card ${isFlipped ? "flipped" : ""}`} onClick={handleClick}>
      <div className="card-inner">
        <div className="card-front">
          <span>{card.img}</span>
        </div>
        <div className="card-back">?</div>
      </div>
    </div>
  );
};

export default Card;
