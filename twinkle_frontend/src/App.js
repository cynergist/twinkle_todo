import React, { Component } from 'react';

class App extends Component {
    state = {
        tasks: []
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/api/');
            const tasks = await res.json();
            this.setState({
                tasks
            });
        } catch (e) {
            console.log(e);
        }
    }
                      
        render() {
            return (
                    <div>
                    {this.state.tasks.map(item => (
                            <div key={item.id}>
                            <h1>{item.text}</h1>
                            <span>{item.description}</span>
                            </div>
                    ))}
                </div>
            );
        }
    }

export default App;
