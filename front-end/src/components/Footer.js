import React from 'react';
import './Footer.css'
// import logo from "../components/images/raptor_maps_logo.png";

function Footer() {
    return (
        <div className="page-container">
            <div className="content-wrap">
                <footer align="center">
                    <div className="socialbtns">
                        <ul>
                            <li><a href="https://github.com/BrokenImage/raptor" className="fa fa-lg fa-github"></a></li>
                        </ul>
                    </div>
                    &copy;{new Date().getFullYear()} Sonomaly | All rights reserved | Terms of Service | Privacy
                 </footer>

            </div>
        </div>


    );
}

export default Footer;