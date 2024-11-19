import React from "react";
import { useState } from "react";
import shortid from "shortid";

function Header({ addTodo }) {
  const [text, setText] = useState("");
  const handleChange = (evt) => {
    setText(evt.target.value);
  };

  const handleSubmit = (evt) => {
    evt.preventDefault();
    addTodo({
      id: shortid.generate(),
      text: text,
      complete: false,
    });
    setText("");
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="add item"
          value={text}
          onChange={handleChange}
        ></input>
        <button onClick={handleSubmit}>add To Do</button>
      </form>
    </div>
  );
}

export default Header;
