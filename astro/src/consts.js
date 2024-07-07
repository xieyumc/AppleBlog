export const SITE_URL = "https://github.com/xieyumc/AppleBlog";

export async function getConfig() {

    const defaultConfig = {
        SITE_TITLE: '鱼鱼幼稚园',
        SITE_DESCRIPTION: '记录鱼鱼的随笔',
        Footer1_Title: '导航',
        Footer1_Website1_title: '首页',
        Footer1_Website1_url: '/',
        Footer1_Website2_title: '目录',
        Footer1_Website2_url: '/archive',
        Footer2_Title: '仓库',
        Footer2_Website1_title: 'GitHub',
        Footer2_Website1_url: 'https://github.com/xieyumc/AppleBlog',
        Footer3_Title: '作者',
        Footer3_Website1_title: '宇宇',
        Footer3_Website1_url: 'https://github.com/xieyumc'
    };

    try {
        const response = await fetch(process.env.WEBCONFIG_API_URL || 'http://127.0.0.1:8000/api/web_config');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Failed to fetch config, using default.', error);
        return defaultConfig;
    }
}

// 调用 getConfig 并导出配置
export const config = await getConfig();