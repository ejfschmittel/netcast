import React from 'react'


const SpotifyEmbed = ({spotifyId, ...other}) => {
    return (
        <div className="spotify-embed">
             <iframe 
                src="https://open.spotify.com/embed/episode/2K1EjgzHGcbu1Sjgw02cNP" 
                width="300" 
                frameborder="0" 
                allowtransparency="true" 
                allow="encrypted-media" 
             />
        </div>
    )
}

export default SpotifyEmbed