document.addEventListener("DOMContentLoaded", () => {
  const gridContainer = document.getElementById("grid-container");
  const contentViewer = document.getElementById("content-viewer");
  const content = document.getElementById("content");
  const closeViewer = document.getElementById("close-viewer");

  // Fetch all HTML files in the pages folder
  fetch("public/links.json")
    .then((response) => response.json())
    .then((links) => {
      links.forEach((filePath, index) => {
        // Extract file name as title
        const title = `Writeup ${index + 1}`;

        // Create a button for each file
        const button = document.createElement("button");
        button.textContent = title;

        // Add click event to load and display content
        button.addEventListener("click", () => {
          fetch(filePath)
            .then((response) => response.text())
            .then((html) => {
              content.innerHTML = html;
              contentViewer.classList.remove("hidden");
            })
            .catch((error) => console.error("Error loading page:", error));
        });

        // Append button to grid container
        gridContainer.appendChild(button);
      });
    })
    .catch((error) => console.error("Error loading links.json:", error));

  // Close the viewer
  closeViewer.addEventListener("click", () => {
    contentViewer.classList.add("hidden");
    content.innerHTML = ""; // Clear content to save resources
  });
});
