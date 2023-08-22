import kue from "kue";
const queue = kue.createQueue();
const job_data = {
  phoneNumber: "",
  message: "",
};
const job = queue.create("push_notification_code", job_data).save((err) => {
  if (!err) console.log("Notification job created:", job.id);
});
job
  .on("complete", (result) => {
    console.log("Notification job completed");
  })
  .on("failed", (result) => {
    console.log("Notification job failed");
  });
