// src/App.js
import React from 'react';
import SimpleGame from './SimpleGame';

function App() {
  return (
    <div style={styles.container}>
      <h1>Welcome to the Simple Canvas Game</h1>
      <SimpleGame />
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    fontFamily: 'Arial, sans-serif',
    backgroundColor: '#282c34',
    color: 'white',
  },
};

export default App;

