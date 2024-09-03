import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles.css";
import { Modal, Button } from "react-bootstrap";

function CreateSubjectForm() {
  const [name, setName] = useState("");
  const [parent, setParent] = useState("");
  const [subjects, setSubjects] = useState([]);
  const [error, setError] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [modalMessage, setModalMessage] = useState("");

  // Function to fetch subjects
  const fetchSubjects = async () => {
    try {
      console.log("Fetching subjects...");
      const response = await axios.get("http://localhost:8000/api/subjects/");
      console.log("Subjects fetched:", response.data);
      setSubjects(response.data);
    } catch (error) {
      console.error("There was an error fetching the subjects:", error);
    }
  };

  // Fetch subjects when the component mounts
  useEffect(() => {
    fetchSubjects();
  }, []);

  // Handle form submission
  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("Form submitted");

    const subjectData = {
      name: name,
      parent: parent || null,
    };

    try {
      console.log("Adding subject...", subjectData);
      const response = await axios.post(
        "http://localhost:8000/api/add-subject/",
        subjectData
      );
      console.log("Subject added successfully:", response.data);
      setModalMessage("Subject added successfully");
      setShowModal(true);
      setName("");
      setParent("");
      setError(null);
    } catch (error) {
      console.error("Error occurred while adding subject:", error);
      if (error.response && error.response.data) {
        setModalMessage("There was an error adding the subject.");
        setError(error.response.data);
      } else {
        setModalMessage("There was an error adding the subject!");
      }
      setShowModal(true);
    }
  };

  // Handle closing of the modal
  const handleCloseModal = () => setShowModal(false);

  return (
    <div className="container mt-5">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            className="form-control"
            id="name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
          {error && error.name && (
            <div className="text-danger">{error.name}</div>
          )}
        </div>
        <div className="form-group">
          <label htmlFor="parent">Parent (optional):</label>
          <select
            className="form-control"
            id="parent"
            value={parent}
            onChange={(e) => setParent(e.target.value)}
            onFocus={fetchSubjects} // Fetch subjects when the dropdown is focused
          >
            <option value="">None</option>
            {subjects.map((subject) => (
              <option key={subject.subject_id} value={subject.subject_id}>
                {subject.name}
              </option>
            ))}
          </select>
        </div>
        <button type="submit" className="btn btn-primary mt-3">
          Add Subject
        </button>
      </form>

      <Modal show={showModal} onHide={handleCloseModal}>
        <Modal.Header closeButton>
          <Modal.Title>Submission Status</Modal.Title>
        </Modal.Header>
        <Modal.Body>{modalMessage}</Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleCloseModal}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default CreateSubjectForm;
