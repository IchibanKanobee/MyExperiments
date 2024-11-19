import React from "react";

function LiftStateIncreaseCount({ count, increaseCount }) {
  return (
    <div>
      <button onClick={increaseCount}>Increase Lifted State</button>
    </div>
  );
}

export default LiftStateIncreaseCount;
