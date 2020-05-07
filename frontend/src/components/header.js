import React from 'react'
import {Link} from "react-router-dom";

import ThemeSwitcher from "./theme-switcher"

const Header = () => {
    return (
        <header className="main-header">
            <Link to="/" className="main-header__title">
                Covcast
            </Link>

            <nav className="main-menu">
                <ul>
   
                    <li><Link className="main-menu__item" to="/podcasts/">podcasts</Link></li>
            
                </ul>
            </nav>

            <ThemeSwitcher className="main-header__theme-toggler" />

        </header>
    )
}

export default Header;