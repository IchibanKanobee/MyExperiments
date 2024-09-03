import React, { useState } from "react";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";
import PauseButton from "./PauseButton";
import PlayButton from "./PlayButton";
import SettingsButton from "./SettingsButton";

const red = "#f54e4e";
const green = "4aec8c";

function Timer() {
  const [isPaused, setIsPaused] = useState(true);

  return (
    <div>
      <CircularProgressbar
        value={60}
        text={"60%"}
        styles={buildStyles({
          textColor: "#fff",
          pathColor: red,
          trailColor: "rgba(255,255,255,.2)",
        })}
      />
      <div style={{ marginTop: "20px" }}>
        {isPaused ? (
          <PauseButton
            onClick={() => {
              setIsPaused(false);
            }}
          />
        ) : (
          <PlayButton
            onClick={() => {
              setIsPaused(true);
            }}
          />
        )}
      </div>
      <div style={{ marginTop: "20px" }}>
        <SettingsButton onClick={() => {}} />
      </div>
    </div>
  );
}

export default Timer;
