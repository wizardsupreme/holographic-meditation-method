// src/pages/index.tsx
import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout description="Transform your consciousness through meditation">
      <main>
        <div className="hero">
          <div className="container">
            <h1 className="hero__title">{siteConfig.title}</h1>
            <p className="hero__subtitle">{siteConfig.tagline}</p>
            <div className="buttons">
              <Link
                className="button button--primary button--lg"
                to="/events">
                Join Our Next Session
              </Link>
            </div>
          </div>
        </div>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}