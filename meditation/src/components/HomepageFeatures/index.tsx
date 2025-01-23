// src/components/HomepageFeatures/index.tsx
import React from 'react';
import styles from './styles.module.css';

interface FeatureItem {
  title: string;
  description: JSX.Element;
  image: string;
}

const FeatureList: FeatureItem[] = [
  {
    title: 'Weekly Free Sessions',
    description: (
      <>
        Join our free weekly meditation sessions in Lisbon. Perfect for beginners and experienced practitioners.
      </>
    ),
    image: 'img/meditation-weekly.svg',
  },
  {
    title: 'Monthly Workshops',
    description: (
      <>
        Deep dive into meditation techniques with our intensive monthly workshops.
      </>
    ),
    image: 'img/meditation-workshop.svg',
  },
  {
    title: 'Bali Retreats',
    description: (
      <>
        Transform your practice with our exclusive Bali meditation retreats.
      </>
    ),
    image: 'img/meditation-retreat.svg',
  },
];

function Feature({title, description, image}: FeatureItem) {
  return (
    <div className={styles.featureItem}>
      <div className={styles.featureImage}>
        <img src={image} alt={title} />
      </div>
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className={styles.featureGrid}>
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}