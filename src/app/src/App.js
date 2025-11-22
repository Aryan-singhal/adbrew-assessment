import React, { useState, useEffect } from 'react';
import './App.css';

export function App() {
  const [todos, setTodos] = useState([]);

  const [description, setDescription] = useState("");

  const fetchTodos = async () => {
    try {
      const response = await fetch('http://localhost:8000/todos/');
      if (response.ok) {
        const data = await response.json();
        setTodos(data);
      }
    } catch (error) {
      console.error("Error fetching todos:", error);
    }
  };

  useEffect(() => {
    fetchTodos();
  }, []);

  
  const handleSubmit = async (e) => {
    e.preventDefault(); 

    if (!description.trim()) return; 

    try {
      
      const response = await fetch('http://localhost:8000/todos/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ description: description }),
      });

      if (response.ok) {
        setDescription(""); 
        fetchTodos();       
      }
    } catch (error) {
      console.error("Error creating todo:", error);
    }
  };

  return (
    <div className="App">
      <div>
        <h1>List of TODOs</h1>
       
        <ul>
          {todos.map((todo) => (
            
            <li key={todo._id}>{todo.description}</li>
          ))}
        </ul>
      </div>
      
      <div>
        <h1>Create a ToDo</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="todo">ToDo: </label>
            <input 
              type="text" 
              id="todo"
              value={description}
              onChange={(e) => setDescription(e.target.value)} 
            />
          </div>
          <div style={{ marginTop: "5px" }}>
            <button type="submit">Add ToDo!</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default App;