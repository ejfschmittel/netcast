import React from 'react'

import EpisodeListItem from "./episode-list-item.component"

const EpisodeList = ({episodes, message="No Episodes found"}) => {
    console.log(episodes.length)
    return (
        <div className="episode-list">
             {
                episodes.length == 0 ? "test" :
                episodes.map((episode) => {
                    return <EpisodeListItem key={episode.id} episode={episode} />
                })  
             }
        </div>
    )
}

export default EpisodeList