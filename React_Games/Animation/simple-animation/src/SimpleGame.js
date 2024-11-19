// src/SimpleGame.js
import React, { useEffect, useRef } from 'react';

function SimpleGame() {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');

    // Initial position and velocity for the square
    let x = 50;
    let y = 50;
    let dx = 2; // Horizontal velocity
    let dy = 2; // Vertical velocity
    const squareSize = 50;

    const render = () => {
      // Clear the canvas
      context.clearRect(0, 0, canvas.width, canvas.height);

      // Draw the square
      context.fillStyle = 'blue';
      context.fillRect(x, y, squareSize, squareSize);

      // Update the square's position
      x += dx;
      y += dy;

      // Bounce off the edges
      if (x + squareSize > canvas.width || x < 0) {
        dx = -dx; // Reverse horizontal direction
      }
      if (y + squareSize > canvas.height || y < 0) {
        dy = -dy; // Reverse vertical direction
      }

      // Request the next animation frame
      requestAnimationFrame(render);
    };

    // Start the animation
    render();

    // Clean up on component unmount
    return () => cancelAnimationFrame(render);
  }, []);

  return <canvas ref={canvasRef} width={500} height={500} />;
}

export default SimpleGame;

