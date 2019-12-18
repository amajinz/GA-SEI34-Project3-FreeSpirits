
import React from 'react';
import { Fade } from 'react-slideshow-image';
import styled from 'styled-components'

const fadeImages = [
    '/static/image/1.jpg',
    '/static/image/2.jpg',
    '/static/image/3.jpg',
    '/static/image/4.jpg',
    '/static/image/5.jpg',
];

const fadeProperties = {
    duration: 5000,
    transitionDuration: 1000,
    infinite: true,
    indicators: false,
    arrows: false,
    onChange: (oldIndex, newIndex) => {
        console.log(`fade transition from ${oldIndex} to ${newIndex}`);
    }
}

const Container = styled.div`
    width: 100%;
    height: 89vh;

    div {
        width: 100;
        height: 89vh;
    }
  
    img {
        width: 100%;
        height: auto;
    }
  `;

const SlideShow = () => {
    return (
        <Container>
            <Fade {...fadeProperties}>
                {fadeImages.map(img => (
                    <div>
                        <img src={img} />
                    </div>
                ))}
            </Fade>
        </Container >
    )
}
export default SlideShow;