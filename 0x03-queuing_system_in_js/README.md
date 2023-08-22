# 0x03-queuing_system_in_js

# Table Of contents

- [0x03-queuing_system_in_js](#0x03-queuing_system_in_js)
- [Table Of contents](#table-of-contents)
  - [Resources](#resources)
  - [Why subscribe?](#why-subscribe)
  - [Understanding the need for seperate job creator and processor](#understanding-the-need-for-seperate-job-creator-and-processor)
    - [Example with code](#example-with-code)
  - [Basically like a task management app](#basically-like-a-task-management-app)

## Resources

[Using redis nodejs](https://www.sitepoint.com/using-redis-node-js/)

## Why subscribe?

Subscribing to a Redis pub/sub channel has several use cases and advantages in various application scenarios. Here are some key points that highlight the purpose and benefits of subscribing to a database channel:

    Real-Time Communication: Subscribing to a channel enables real-time communication between different parts of an application or between different applications altogether. It allows clients to be instantly notified when relevant events occur, without the need for constant polling.

    Decoupling Components: By using pub/sub, components of a system can be decoupled. Publishers and subscribers don't need to have direct knowledge of each other. This promotes a modular and flexible architecture, making it easier to add, modify, or remove components without affecting the entire system.

    Event Broadcasting: Pub/sub is ideal for broadcasting events to multiple subscribers. For example, if you have multiple instances of an application running and you want all of them to be aware of certain events (e.g., user login, new data availability), pub/sub simplifies event distribution.

    Notifications: Subscribing to channels allows you to implement notification systems. For instance, in a social media platform, you can use pub/sub to notify users about new messages, likes, comments, etc., in real time.

    Caching Invalidation: Subscribing to channels can help with cache invalidation. When certain data changes, you can publish a message to a channel, and subscribers can respond by updating their caches accordingly.

    Distributed Systems: In distributed systems, pub/sub can be used to keep different components or nodes synchronized. When an action occurs on one node, it can publish an event, and all other nodes that are subscribers will be notified.

    Multi-Service Communication: In a microservices architecture, different services can communicate with each other via pub/sub. This allows services to remain independent while still being able to share information and react to events.

    Load Balancing and Scaling: Subscribers can be distributed across multiple instances or nodes, allowing for load balancing and scalability. This can be useful for handling a high volume of incoming events.

    Reduced Latency: Compared to polling for changes, pub/sub reduces latency because clients receive events as soon as they occur, rather than waiting for a scheduled poll.

    Flexible Topologies: With pub/sub, you can set up various communication topologies, such as one-to-many (broadcast), one-to-one, and many-to-many, to suit the requirements of your application.

In summary, subscribing to a database channel through Redis pub/sub provides a flexible and efficient way to implement real-time communication, event propagation, and coordination between different parts of an application or even different applications in a distributed environment. It promotes modularity, scalability, and responsiveness in software systems.

## Understanding the need for seperate job creator and processor

**Analogy: The Restaurant Kitchen**

Imagine you're running a restaurant with a busy kitchen that prepares and serves food to customers. In this analogy:

- The **Job Creator** is equivalent to the waiter who takes orders from customers and passes them to the kitchen.

- The **Job Consumer** is akin to the chefs in the kitchen who prepare the orders and send them out to the dining area.

Now, let's explore the benefits of this separation:

1. **Specialization and Efficiency:**

   Just like how chefs are specialized in cooking and waiters are specialized in serving, having separate job creators and consumers allows each part of your application to focus on its primary task. Job creators can concentrate on gathering data and creating jobs, while job consumers can focus on efficiently processing those jobs.

2. **Scalability:**

   Imagine your restaurant is getting busier, and you need to handle more orders. Adding more chefs to the kitchen (job consumers) allows you to process more orders concurrently without overwhelming the waiters (job creators).

3. **Responsiveness:**

   If the kitchen (job consumers) gets backed up with orders, it won't affect the waiters' ability to take new orders. Similarly, if a chef is working on a complex dish, it won't prevent the waiter from taking more orders and serving other tables.

4. **Error Isolation:**

   If a dish is prepared incorrectly or takes longer than expected, it won't affect the waiter's ability to continue taking orders and serving other tables. The kitchen (job consumers) can handle errors and retries without impacting the overall restaurant operation.

5. **Resource Allocation:**

   Chefs need various resources, such as ingredients and cooking utensils. By having a separate kitchen (job consumers), you can allocate specific resources for job processing without affecting other parts of your application.

6. **Flexibility:**

   If you want to introduce new dishes (job types) or modify the way you prepare existing dishes, you can do so in the kitchen (job consumers) without changing how the waiters (job creators) take orders and interact with customers.

In this analogy, having separate job creators and consumers (like waiters and chefs) allows your application to be more efficient, scalable, and responsive. Just as a restaurant's waitstaff and kitchen staff work together seamlessly to deliver a great dining experience, job creators and consumers collaborate to handle tasks efficiently in your application.

Remember, as your application's complexity grows, the benefits of this separation become more pronounced, making it easier to manage and maintain the various components.

### Example with code

Let's translate the restaurant analogy into code using job creators and consumers. We'll simulate a simple scenario where customers place food orders, and the kitchen processes those orders in the background.

**Step 1: Setting Up the Environment**

Install the "kue" library by running:

```sh
npm install kue
```

**Step 2: Creating a Job Creator (Waiter)**

Create a file named `orderCreator.js`:

```javascript
const kue = require("kue");
const queue = kue.createQueue();

const orders = [
  { table: 1, dish: "Pasta" },
  { table: 2, dish: "Burger" },
  { table: 1, dish: "Salad" },
];

orders.forEach((order) => {
  const jobData = {
    table: order.table,
    dish: order.dish,
  };

  const orderJob = queue.create("prepareDish", jobData).save(function (err) {
    if (!err) {
      console.log(`Order for table ${order.table} created: ${orderJob.id}`);
    }
  });
});
```

**Step 3: Creating a Job Consumer (Chef)**

Create a file named `orderProcessor.js`:

```javascript
const kue = require("kue");
const queue = kue.createQueue();

queue.process("prepareDish", function (job, done) {
  const { table, dish } = job.data;

  // Simulate preparing the dish
  console.log(`Preparing ${dish} for table ${table}...`);
  setTimeout(() => {
    console.log(`${dish} for table ${table} is ready.`);
    done();
  }, Math.random() * 3000); // Simulate varying cooking times
});
```

**Step 4: Running the Example**

In one terminal window, run the job processor (chef):

```sh
node orderProcessor.js
```

In another terminal window, run the job creator (waiter):

```sh
node orderCreator.js
```

You'll see output in the job processor terminal indicating that orders are being processed by the "chef." The job creator terminal will show orders being created by the "waiter."

This example demonstrates the separation of job creation (order creation) and job processing (order preparation) in a restaurant analogy. The job creator (waiter) takes orders and creates jobs, while the job processor (chef) processes those jobs (orders) in the background.

Remember that in a real-world application, job consumers could be running on separate machines or containers to achieve better scalability and resource management.

## Basically like a task management app

Yes, that's a great way to think about it! Job queues like Kue can be likened to task management applications where tasks (jobs) are created and then assigned to different workers (consumers) for processing. Just as task management applications help teams organize and prioritize their work, job queues help applications manage and distribute tasks in an efficient and scalable manner.

In a task management application, you might have tasks that need to be assigned to specific team members based on their expertise or availability. Similarly, in a job queue system:

- **Job Creator (Task Creator):** This is where tasks (jobs) are created. These tasks can represent various types of work that need to be done.

- **Job Consumer (Worker):** This is the worker who performs the actual work associated with the task. The workers can be specialized to handle specific types of tasks or can be dynamically assigned tasks based on availability and expertise.

Just like task management applications help teams collaborate and ensure tasks are completed efficiently, job queues ensure that background tasks in an application are processed reliably, without blocking the main application's responsiveness.

The separation of job creation and processing allows for specialization, scalability, and efficient resource utilization, just as assigning tasks to different team members allows each person to focus on their strengths and work together effectively.
