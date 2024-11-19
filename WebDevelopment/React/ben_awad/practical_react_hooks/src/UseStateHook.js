import React from "react";
import { useState } from "react";

function UseStateHook() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>increase count</button>
    </div>
  );
}

export default UseStateHook;
