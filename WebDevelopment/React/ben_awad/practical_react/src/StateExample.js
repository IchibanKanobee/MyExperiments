import React from "react";
import { useState } from "react";

function StateExample() {
  const [count, setCount] = useState(0);
  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <div>StateExample {count}</div>
      <button onClick={handleClick}>Increase</button>
    </div>
  );
}

export default StateExample;
