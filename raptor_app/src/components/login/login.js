import React from "react";
import loginImg from "../../login.svg";

export class login extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className='base-container' ref={this.props.containerRef}>
                <div className='header'>Login</div>
                <div classname='content'>
                    <div className='image'>
                        <img src={loginImg} />
                    </div>
                </div>
            </div>
        )
    }
}