import "./App.css";
import PropsExample from "./PropsExample";
import StateExample from "./StateExample";
import FetchAPI from "./FetchAPI";
import FetchAPIMultipleImages from "./FetchAPIMultipleImages";
import LiftStateIncreaseCount from "./LiftStateIncreaseCount.js";
import LiftStateDecreaseCount from "./LiftStateDecreaseCount.js";
import LiftStateShowCount from "./LiftStateShowCount.js";

import { useState } from "react";

function App() {
  const [count, setCount] = useState(5);

  const increaseCount = () => {
    setCount(count + 1);
  };

  const decreaseCount = () => {
    setCount(count - 1);
  };

  return (
    <div className="App">
      Hello
      <PropsExample name="Dave" age={40} />
      <StateExample />
      <FetchAPI />
      <FetchAPIMultipleImages />
      <LiftStateIncreaseCount count={count} increaseCount={increaseCount} />
      <LiftStateDecreaseCount count={count} decreaseCount={decreaseCount} />
      <LiftStateShowCount count={count} />
      <LiftStateShowCount count={count} />
      <LiftStateShowCount count={count} />
    </div>
  );
}

export default App;
