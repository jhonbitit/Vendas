"use client";

import { useEffect } from "react";

type Props = {
  pageUrl?: string;
  showChat?: boolean;
};

export default function FacebookEmbed({ pageUrl, showChat }: Props) {
  useEffect(() => {
    // Carrega SDK do Facebook
    const id = "facebook-jssdk";
    if (document.getElementById(id)) return;
    const js = document.createElement("script");
    js.id = id;
    js.src = "https://connect.facebook.net/pt_BR/sdk.js#xfbml=1&version=v20.0";
    const first = document.getElementsByTagName("script")[0];
    first?.parentNode?.insertBefore(js, first);
  }, []);

  const pageHref = pageUrl || process.env.NEXT_PUBLIC_FB_PAGE_URL || "https://www.facebook.com/facebook";
  const enableChat = showChat ?? (process.env.NEXT_PUBLIC_FB_CHAT_ENABLED === "true");

  return (
    <div className="space-y-4">
      <div className="fb-page" data-href={pageHref} data-tabs="timeline" data-width="1000" data-height="600" data-small-header="false" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true"></div>
      {enableChat && (
        <div id="fb-root"></div>
      )}
    </div>
  );
}