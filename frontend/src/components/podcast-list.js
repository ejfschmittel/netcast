import React from 'react'
import {Link} from "react-router-dom"

const PodcastList = ({loading, data}) => {
    console.log(data)
    return (
        <div className="podcast-list">
            {loading ? "loading podcasts..." : 
                data ? 
                    data.allPodcasts.map((podcast) => (
                        <PodcastItem podcast={podcast} />
                    ))
                : "no podcasts found"            
            }

        </div>
    )
}

const PodcastItem = ({podcast}) => {
    return (
        <Link className="podcast-item" to={`/podcasts/${podcast.id}`}>
            <img src="https://www.datenschutz-guru.de/wp-content/uploads/2019/06/podcast_pic_post.9c44d265977a496d859d68358214c4d2.jpg"/>
            <div className="podcast-item__info">
                <h4>{podcast.name}</h4>
                <p>
                    some text some text
                    some text some text
                    some text some text
                    some text some text
                    some text some text
                    some text some text
                    some text some text
                    some text some text
                    some text some text
                </p>
            </div>


            <div className="podcast-item__categories">
                <ul>
                    <li>
                        <Link>#science</Link>
                    </li>
                    <li>
                        <Link>#nature</Link>
                    </li>
                </ul>
            </div>
      
        </Link>
    )
}

export default PodcastList