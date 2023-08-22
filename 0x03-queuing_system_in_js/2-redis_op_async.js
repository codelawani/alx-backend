import { createClient } from "redis";
import redis from "redis";
import { promisify } from "util";
const client = createClient();
client
  .on("error", (err) => {
    console.error("Redis client not connected to the server:", err.message);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });
const asyncGet = promisify(client.get).bind(client);
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}
async function displaySchoolValue(schoolName) {
  const reply = await asyncGet(schoolName);
  console.log(reply);
}
(async () => {
  await displaySchoolValue("Holberton");
  setNewSchool("HolbertonSanFrancisco", "100");
  await displaySchoolValue("HolbertonSanFrancisco");
})();
