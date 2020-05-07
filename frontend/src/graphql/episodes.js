import {gql} from "apollo-boost"


const PODCAST_EPISODES = gql`
    query Podcast($podcastId: Int!){
        podcastEpisodes(podcastId: $podcastId){
            id,
            title,
            episodeNum,
            podcast{
                id,
                name
            }
        }
    }
`;

const PODCAST_EPISODE = gql`
    query PodcastEpisode($podcastId: Int!, $episodeNum: Int){
        podcastEpisode(podcastId: $podcastId, episodeNum: $episodeNum){
            id,
            title,
            youtubeId
        }
    }
`;

export default {
    PODCAST_EPISODES,
    PODCAST_EPISODE
}