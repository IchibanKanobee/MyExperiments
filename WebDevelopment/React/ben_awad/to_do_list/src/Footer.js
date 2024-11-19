import React from "react";

function Footer({
  items,
  setShow,
  handleDeleteCompleted,
  handleToggleAllComplete,
}) {
  return (
    <div>
      <div>Todos left: {items.filter((item) => !item.complete).length}</div>;
      <button onClick={() => setShow("all")}>all</button>
      <button onClick={() => setShow("active")}>active</button>
      <button onClick={() => setShow("complete")}>complete</button>
      {/* {items.filter((item) => item.complete).length ? ( */}
      {items.some((item) => item.complete) ? (
        <div>
          <button onClick={() => handleDeleteCompleted()}>
            delete completed items
          </button>
        </div>
      ) : null}
      <div>
        <button onClick={() => handleToggleAllComplete()}>
          toggle all complete
        </button>
      </div>
    </div>
  );
}

export default Footer;
