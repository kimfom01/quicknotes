deleteNote = (noteId) => {
  try {
    fetch("/delete-note", {
      method: "DELETE",
      body: JSON.stringify({ noteId }),
    }).then((result) => {
      if (result.status !== 204) {
        throw new Error("Unable to delete");
      }
      window.location.reload();
    });
  } catch (err) {
    console.error(err);
  }
};
