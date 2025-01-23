// docusaurus.config.ts
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Holographic Meditation Method',
  tagline: 'Transform Your Consciousness',
  url: 'https://meditation.exponentials.studio',
  baseUrl: '/',
  favicon: 'img/favicon.ico',
  organizationName: 'wizardsupreme',
  projectName: 'holographic-meditation-method',
  
  presets: [
    [
      'classic',
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.ts'),
          routeBasePath: '/',
          path: 'docs',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }) satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'Holographic Meditation',
      logo: {
        alt: 'Meditation Logo',
        src: 'img/logo.svg',
      },
      items: [
        {to: '/events', label: 'Events', position: 'right'},
        {to: '/workshops', label: 'Workshops', position: 'right'},
        {to: '/retreat', label: 'Retreat', position: 'right'},
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Community',
          items: [
            {
              label: 'WhatsApp Group',
              href: '#',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Holographic Meditation Method`,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;