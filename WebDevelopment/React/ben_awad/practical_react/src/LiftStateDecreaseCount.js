import React from "react";

function LiftStateDecreaseCount({ count, decreaseCount }) {
  return (
    <div>
      <button onClick={decreaseCount}>Decrease Lifted State</button>
    </div>
  );
}

export default LiftStateDecreaseCount;
