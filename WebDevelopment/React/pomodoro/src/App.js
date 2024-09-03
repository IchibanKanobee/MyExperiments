import React from "react";
import "./App.css";
import Settings from "./Settings";
import Timer from "./Timer";
import { useState } from "react";

function App() {
  const [showSettings, setShowSettings] = useState(false);
  return <main>{showSettings ? <Settings /> : <Timer />}</main>;
}

export default App;
