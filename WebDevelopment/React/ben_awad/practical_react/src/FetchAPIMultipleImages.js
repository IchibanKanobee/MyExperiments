import React from "react";
import { useState, useEffect } from "react";

function FetchAPIMultipleImages() {
  const [loading, setLoading] = useState(true);
  const [people, setPeople] = useState([]);

  //https://www.copycat.dev/blog/react-fetch/
  // Note: the empty deps array [] means
  // this useEffect will run once
  // similar to componentDidMount()
  useEffect(() => {
    const url = "https://api.randomuser.me/?results=3";
    fetch(url)
      .then((res) => res.json())
      .then(
        (result) => {
          setLoading(false);
          setPeople(result.results);
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          //          setLoading(true);
        }
      );
  }, []);

  if (loading) return <div> loading... </div>;

  if (!people.length) return <div> didn't get a person </div>;

  return (
    <div>
      {people.map((person) => (
        <div key={person.login.uuid}>
          <div>First Name: {person.name.first}</div>
          <div>Last Name: {person.name.last}</div>
          <div>
            <img src={person.picture.large}></img>
          </div>
        </div>
      ))}
    </div>
  );
}
export default FetchAPIMultipleImages;
