document.addEventListener("DOMContentLoaded", function () {
  const serverAddress = "172.28.146.91:8188";
  const comfyClient = new ComfyClient(serverAddress);
  comfyClient.init();
});
