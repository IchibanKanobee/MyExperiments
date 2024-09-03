// CreateQuestionForm.js

import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles.css"; // Import the existing styles

const CreateQuestionForm = () => {
  const [questionText, setQuestionText] = useState("");
  const [answerText, setAnswerText] = useState("");
  const [image, setImage] = useState(null);
  const [video, setVideo] = useState(null);
  const [subject, setSubject] = useState("");
  const [subjects, setSubjects] = useState([]);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch subjects from the API when the component mounts
    const fetchSubjects = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/subjects/");
        setSubjects(response.data);
      } catch (err) {
        setError("Failed to fetch subjects. Please try again.");
      }
    };

    fetchSubjects();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsSubmitting(true);
    setError(null);

    const formData = new FormData();
    formData.append("question_text", questionText);
    formData.append("answer_text", answerText);
    if (image) formData.append("image", image);
    if (video) formData.append("video", video);
    formData.append("subject", subject);

    try {
      await axios.post("http://localhost:8000/api/add-question/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      // Handle success (e.g., show a success message or redirect)
      alert("Question created successfully!");
      setQuestionText("");
      setAnswerText("");
      setImage(null);
      setVideo(null);
      setSubject("");
    } catch (err) {
      setError("Failed to create question. Please try again.");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="container">
      <h1>Create a New Question</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="questionText">Question Text:</label>
          <textarea
            id="questionText"
            className="form-control large-textarea"
            value={questionText}
            onChange={(e) => setQuestionText(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="answerText">Answer Text:</label>
          <textarea
            id="answerText"
            className="form-control large-textarea"
            value={answerText}
            onChange={(e) => setAnswerText(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="image">Image:</label>
          <input
            id="image"
            type="file"
            className="form-control-file"
            accept="image/*"
            onChange={(e) => setImage(e.target.files[0])}
          />
        </div>
        <div>
          <label htmlFor="video">Video:</label>
          <input
            id="video"
            type="file"
            className="form-control-file"
            accept="video/*"
            onChange={(e) => setVideo(e.target.files[0])}
          />
        </div>
        <div>
          <label htmlFor="subject">Subject:</label>
          <select
            id="subject"
            className="form-control"
            value={subject}
            onChange={(e) => setSubject(e.target.value)}
            required
          >
            <option value="" disabled>
              Select a subject
            </option>
            {subjects.map((subj) => (
              <option key={subj.subject_id} value={subj.subject_id}>
                {subj.name} {/* Adjust based on your API response */}
              </option>
            ))}
          </select>
        </div>
        <button
          type="submit"
          className="btn btn-primary"
          disabled={isSubmitting}
        >
          {isSubmitting ? "Submitting..." : "Submit"}
        </button>
        {error && <p className="text-danger">{error}</p>}
      </form>
    </div>
  );
};

export default CreateQuestionForm;
