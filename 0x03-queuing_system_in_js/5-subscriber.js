import redis from "redis";
const subscriber = redis.createClient();
subscriber
  .on("error", (err) => {
    console.error("Redis client not connected to the server:", err.message);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });

subscriber.subscribe("holberton school channel");
subscriber.on("message", (err, reply) => {
  if (reply === "KILL_SERVER") {
    subscriber.unsubscribe();
    subscriber.quit();
  }
  console.log(reply);
});
