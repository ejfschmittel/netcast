import React from 'react'


const YoutubeEmbed = ({youtubeId, ...other}) => {
    return (
        <div className="youtube-embed">
            <iframe 
            width="560" 
            height="315" 
            src={`https://www.youtube.com/embed/${youtubeId}`}
            frameborder="0" 
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen 
            {...other}
            />

        </div>
    )
}

export default YoutubeEmbed