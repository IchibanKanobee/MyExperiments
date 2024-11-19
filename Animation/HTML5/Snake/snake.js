const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Load images for snake parts
const headImg = new Image();
const tailImg = new Image();
const bodyImg = new Image();
const turnImg = new Image();
const tailTurnImg = new Image();

headImg.src = "head.png";
tailImg.src = "tail.png";
bodyImg.src = "body.png";
turnImg.src = "turn.png";
tailTurnImg.src = "tailTurn.png";

// Game variables
const gridSize = 20;
const canvasWidth = canvas.width;
const canvasHeight = canvas.height;
const directions = {
  UP: { x: 0, y: -1 },
  DOWN: { x: 0, y: 1 },
  LEFT: { x: -1, y: 0 },
  RIGHT: { x: 1, y: 0 },
};
let snake = [
  { x: 5, y: 5, dir: directions.RIGHT }, // Head
  { x: 4, y: 5, dir: directions.RIGHT }, // Body segment
  { x: 3, y: 5, dir: directions.RIGHT }, // Tail
];
let food = { x: 15, y: 10 };
let currentDirection = directions.RIGHT;
let isTurning = false;
let gameOver = false;

// Timer variables
const gameSpeed = 500; // 500 ms per animation cycle
let gameInterval;

let isPaused = false; // Track pause state

// Function to toggle pause state
function togglePause() {
  isPaused = !isPaused;

  // Update button text
  const pauseButton = document.getElementById("pauseButton");
  pauseButton.textContent = isPaused ? "Resume" : "Pause";

  // Stop the game loop if paused
  if (isPaused) {
    clearInterval(gameInterval);
  } else {
    gameInterval = setInterval(gameLoop, gameSpeed); // Resume game loop
  }
}

// Attach event listener to the pause button
document.getElementById("pauseButton").addEventListener("click", togglePause);

// Keyboard controls
window.addEventListener("keydown", (e) => {
  if (isTurning) return;
  if (e.key === "ArrowUp" && currentDirection !== directions.DOWN) {
    currentDirection = directions.UP;
    isTurning = true;
  } else if (e.key === "ArrowDown" && currentDirection !== directions.UP) {
    currentDirection = directions.DOWN;
    isTurning = true;
  } else if (e.key === "ArrowLeft" && currentDirection !== directions.RIGHT) {
    currentDirection = directions.LEFT;
    isTurning = true;
  } else if (e.key === "ArrowRight" && currentDirection !== directions.LEFT) {
    currentDirection = directions.RIGHT;
    isTurning = true;
  }
});

// Game functions
function drawSnake() {
  for (let i = 0; i < snake.length; i++) {
    const segment = snake[i];
    let img = bodyImg; // Default image for body

    // Determine the image type
    if (i === 0) img = headImg; // Head
    else if (i === snake.length - 1) {
      // Tail logic
      const tail = segment;
      const beforeTail = snake[i - 1];
      const prevSegmentDir = beforeTail.dir;
      const tailDir = tail.dir;

      // Determine if the tail is turning
      if (prevSegmentDir !== tailDir) {
        img = tailTurnImg; // Use tail-turn image
        ctx.save();
        const x = tail.x * gridSize;
        const y = tail.y * gridSize;
        ctx.translate(x + gridSize / 2, y + gridSize / 2);

        // Rotate based on direction change
        if (prevSegmentDir === directions.RIGHT && tailDir === directions.UP) {
          ctx.rotate((90 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.UP &&
          tailDir === directions.LEFT
        ) {
          ctx.rotate((180 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.LEFT &&
          tailDir === directions.DOWN
        ) {
          ctx.rotate((-90 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.DOWN &&
          tailDir === directions.RIGHT
        ) {
          ctx.rotate(0);
        } else if (
          prevSegmentDir === directions.RIGHT &&
          tailDir === directions.DOWN
        ) {
          ctx.rotate((-90 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.DOWN &&
          tailDir === directions.LEFT
        ) {
          ctx.rotate((180 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.LEFT &&
          tailDir === directions.UP
        ) {
          ctx.rotate((90 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.UP &&
          tailDir === directions.RIGHT
        ) {
          ctx.rotate(0);
        }

        ctx.drawImage(img, -gridSize / 2, -gridSize / 2, gridSize, gridSize);
        ctx.restore();
        continue;
      }
      img = tailImg; // Straight tail
    } else {
      // Handle turns for body segments
      const prevSegmentDir = snake[i - 1].dir;
      const currSegmentDir = segment.dir;

      if (prevSegmentDir !== currSegmentDir) {
        img = turnImg; // Use turn image
        ctx.save();
        const x = segment.x * gridSize;
        const y = segment.y * gridSize;
        ctx.translate(x + gridSize / 2, y + gridSize / 2);

        // Rotate based on direction change
        if (
          prevSegmentDir === directions.RIGHT &&
          currSegmentDir === directions.UP
        ) {
          ctx.rotate((90 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.UP &&
          currSegmentDir === directions.LEFT
        ) {
          ctx.rotate(0);
        } else if (
          prevSegmentDir === directions.LEFT &&
          currSegmentDir === directions.DOWN
        ) {
          ctx.rotate((-90 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.DOWN &&
          currSegmentDir === directions.RIGHT
        ) {
          ctx.rotate((180 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.RIGHT &&
          currSegmentDir === directions.DOWN
        ) {
          console.log(
            "prevSegmentDir === directions.RIGHT && currSegmentDir === directions.DOWN"
          );
          ctx.rotate((-90 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.DOWN &&
          currSegmentDir === directions.LEFT
        ) {
          console.log(
            "prevSegmentDir === directions.DOWN && currSegmentDir === directions.LEFT"
          );
          ctx.rotate((180 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.LEFT &&
          currSegmentDir === directions.UP
        ) {
          ctx.rotate((-180 * Math.PI) / 180);
        } else if (
          prevSegmentDir === directions.UP &&
          currSegmentDir === directions.RIGHT
        ) {
          ctx.rotate((-90 * Math.PI) / 180);
        }

        ctx.drawImage(img, -gridSize / 2, -gridSize / 2, gridSize, gridSize);
        ctx.restore();
        continue;
      }
    }

    // Draw regular segment (straight body, head, or tail)
    ctx.save();
    const x = segment.x * gridSize;
    const y = segment.y * gridSize;

    if (segment.dir === directions.RIGHT) {
      ctx.translate(x + gridSize / 2, y + gridSize / 2);
      ctx.rotate((90 * Math.PI) / 180);
      ctx.drawImage(img, -gridSize / 2, -gridSize / 2, gridSize, gridSize);
    } else if (segment.dir === directions.LEFT) {
      ctx.translate(x + gridSize / 2, y + gridSize / 2);
      ctx.rotate((-90 * Math.PI) / 180);
      ctx.drawImage(img, -gridSize / 2, -gridSize / 2, gridSize, gridSize);
    } else {
      ctx.drawImage(img, x, y, gridSize, gridSize); // No rotation for vertical movement
    }

    ctx.restore();
  }
}

function drawFood() {
  ctx.fillStyle = "red";
  ctx.fillRect(food.x * gridSize, food.y * gridSize, gridSize, gridSize);
}

function moveSnake() {
  const head = snake[0];
  const newHead = {
    x: head.x + currentDirection.x,
    y: head.y + currentDirection.y,
    dir: currentDirection,
  };

  // Add new head
  snake.unshift(newHead);

  // Check for food
  if (newHead.x === food.x && newHead.y === food.y) {
    spawnFood();
  } else {
    // Remove tail
    snake.pop();
  }

  // Check for collisions
  if (
    newHead.x < 0 ||
    newHead.y < 0 ||
    newHead.x >= canvasWidth / gridSize ||
    newHead.y >= canvasHeight / gridSize ||
    snake.slice(1).some((seg) => seg.x === newHead.x && seg.y === newHead.y)
  ) {
    clearInterval(gameInterval);
    gameOver = true;
    alert("Game Over!");
  }

  isTurning = false;
}

function spawnFood() {
  food = {
    x: Math.floor(Math.random() * (canvasWidth / gridSize)),
    y: Math.floor(Math.random() * (canvasHeight / gridSize)),
  };
}

function gameLoop() {
  if (gameOver) return;
  if (isPaused) return;

  ctx.clearRect(0, 0, canvasWidth, canvasHeight);
  moveSnake();
  drawSnake();
  drawFood();
}

// Start the game
headImg.onload = () => {
  gameInterval = setInterval(gameLoop, gameSpeed);
};
