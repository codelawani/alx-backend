const express = require("express");
import { promisify } from "util";
import { createClient } from "redis";

const app = express();
const port = 1245;

const client = createClient();
const asyncGet = promisify(client.get).bind(client);

const listProducts = [
  {
    itemId: 1,
    itemName: "Suitcase 250",
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: "Suitcase 450",
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: "Suitcase 650",
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: "Suitcase 1050",
    price: 550,
    initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  return listProducts.find((product) => product.itemId == id);
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}
async function getCurrentReservedStockById(itemId) {
  const stock = await asyncGet(`item.${itemId}`);
  return Number(stock);
}

app.get("/list_products", (req, res) => {
  res.json(listProducts);
});
app.get("/list_products/:itemId", async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.json({ status: "Product not found" });
    return;
  }
  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.initialAvailableQuantity - reservedStock;
  res.json({
    ...product,
    currentQuantity: currentQuantity,
  });
});

app.get("/reserve_product/:itemId", async (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);
  if (item === null) {
    res.json({ status: "Product not found" });
    return;
  }

  const currReservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = item.initialAvailableQuantity - currReservedStock;
  if (currentQuantity <= 0) {
    res.json({ status: "Not enough stock available", itemId });
    return;
  }

  reserveStockById(itemId, currReservedStock + 1);
  res.json({ status: "Reservation confirmed", itemId });
});

app.listen(port, () => {
  console.log("Server listening on port", port);
});
