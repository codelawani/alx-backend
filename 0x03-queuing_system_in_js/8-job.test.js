import chai from "chai";
const expect = chai.expect;
import kue from "kue";

import createPushNotificationsJobs from "./8-job.js";
describe("createPushNotificationsJobs", () => {
  let queue;

  beforeEach(() => {
    // Set up a new Kue queue in test mode before each test
    queue = kue.createQueue({ testMode: true });
  });

  afterEach(() => {
    // Clean up the queue after each test
    queue.testMode.clear();
  });

  it("should create jobs in the queue", () => {
    const testJobs = [
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account",
      },
      {
        phoneNumber: "4153518781",
        message: "This is the code 4562 to verify your account",
      },
      // Add more test jobs...
    ];

    console.log(
      "Before calling createPushNotificationsJobs:",
      queue.testMode.jobs
    );

    createPushNotificationsJobs(testJobs, queue);

    console.log(
      "After calling createPushNotificationsJobs:",
      queue.testMode.jobs
    );

    // Assert that the jobs are in the queue
    expect(queue.testMode.jobs.length).to.equal(testJobs.length);
  });

  // Add more test cases as needed...
});
