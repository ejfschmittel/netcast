import React, {useState} from 'react'

import "./theme-switcher.scss"

const ThemeSwitcher = () => {
    const [showDarkTheme, setShowDarkTheme] = useState(false);


    const onToggle = (e) => {
        if(e.target.checked){
            console.log("checked")
            document.documentElement.setAttribute('data-theme', 'dark');
        }else{
            console.log("unchecked")
            document.documentElement.setAttribute('data-theme', 'light');
        }

    }

    return (
        <div className="theme-switch-wrapper">
            <label className="theme-switch" for="checkbox">
                <input type="checkbox" id="checkbox" onChange={onToggle}/>
                <div className="slider round"></div>
            </label>
        <em>Enable Dark Mode!</em>
        </div>
    )
}

export default ThemeSwitcher