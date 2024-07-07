export const SITE_URL = "https://github.com/xieyumc/AppleBlog";


export const SITE_TITLE = `鱼鱼幼稚园`;
export const SITE_DESCRIPTION = '记录鱼鱼的随笔';


export const Footer1_Title = "导航";
export const Footer1_Website1_title = "首页";
export const Footer1_Website1_ulr = "/";
export const Footer1_Website2_title = "目录";
export const Footer1_Website2_ulr = "/archive";

export const Footer2_Title = "仓库";
export const Footer2_Website1_title = "GitHub";
export const Footer2_Website1_ulr = "/";

export const Footer3_Title = "作者";
export const Footer3_Website1_title = "宇宇";
export const Footer3_Website1_ulr = "https://github.com/xieyumc";

export async function getConfig() {

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