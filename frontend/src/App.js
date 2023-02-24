import React, { Component } from 'react';

class App extends Component {
    state = {
        subways: []
    };

  /* async는 promise가 아니어도 반환값을 promise로 감싸서 반환해주는 형식이다.
     await는 async함수 안에서만 사용할 수 있으며 잠시 기다렸다 명령을 행하는 역할을 한다.*/
    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/api/');
            const subways = await res.json();
            this.setState({
                subways
            });
        } catch (e) {
            console.log(e);
        }
    }

    render() {
        return (
            <div>
                {this.state.subways.map(item => (
                    <div key={item.id}>
                        <h1>{item.title}</h1>
                        <span>{item.location}</span>
                    </div>
                ))}
            </div>
        );
    }
}

export default App;