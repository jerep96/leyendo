writeButton.addEventListener("click", async () => {
  console.log("User clicked write button");

  try {
    const ndef = new NDEFReader();
    await ndef.write("Hello world!");
    console.log("> Message written");
  } catch (error) {
    console.log("Argh! " + error);
  }
});
jfd hdbch
