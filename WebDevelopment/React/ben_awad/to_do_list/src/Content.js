import React from "react";
import ToDo from "./ToDo";

function Content({ items, toggleComplete, handleDelete, show }) {
  let showItems = [];
  if (show === "all") {
    showItems = items;
  } else if (show === "active") {
    showItems = items.filter((item) => !item.complete);
  } else {
    showItems = items.filter((item) => item.complete);
  }

  return (
    <div>
      {showItems.map((item) => (
        <ToDo
          key={item.id}
          itemToggleComplete={() => toggleComplete(item.id)}
          onDelete={() => handleDelete(item.id)}
          todo={item}
        />
      ))}
    </div>
  );
}

export default Content;
