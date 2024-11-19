import "./App.css";
import Content from "./Content";
import Header from "./Header";
import Footer from "./Footer";

import { useState } from "react";

function App() {
  const [todos, setTodos] = useState([]);
  const [show, setShow] = useState("all");
  const [toggleAllComplete, setToggleAllComplete] = useState(false);

  const addTodo = (todo) => {
    const newTodos = [todo, ...todos];
    setTodos(newTodos);
  };

  const toggleComplete = (id) => {
    const newTodo = todos.map((todo) => {
      if (todo.id === id) {
        return {
          id: todo.id,
          text: todo.text,
          complete: !todo.complete,
        };
      } else {
        return todo;
      }
    });
    setTodos(newTodo);
  };

  const handleDelete = (id) => {
    const newTodo = todos.filter((todo) => todo.id !== id);
    setTodos(newTodo);
  };

  const handleDeleteCompleted = () => {
    const newTodo = todos.filter((todo) => !todo.complete);
    setTodos(newTodo);
  };

  const handleToggleAllComplete = () => {
    setToggleAllComplete(!toggleAllComplete);
    const newTodo = todos.map((todo) => {
      return {
        ...todo,
        complete: toggleAllComplete,
      };
    });
    setTodos(newTodo);
  };

  return (
    <div className="App">
      <Header addTodo={addTodo} />
      <Content
        items={todos}
        toggleComplete={toggleComplete}
        handleDelete={handleDelete}
        show={show}
      />
      <Footer
        items={todos}
        setShow={setShow}
        handleDeleteCompleted={handleDeleteCompleted}
        handleToggleAllComplete={handleToggleAllComplete}
      />
    </div>
  );
}

export default App;
