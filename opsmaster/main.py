from fastapi import FastAPI
from app import core, router, AppConfig, AppLogger, celery_app


application = FastAPI(
    title=AppConfig.get("app", "title"),
    debug=AppConfig.getboolean("app", "debug"),
    description=AppConfig.get("app", "description")
)


# 事件监听
application.add_event_handler("startup", core.startup(application))
application.add_event_handler("shutdown", core.shutdown(application))


# 路由挂载
application.include_router(router.zone_router)
application.include_router(router.user_router)


if __name__ == "__main__":
    import uvicorn

    # celery_aps = celery_app.start(
    #     argv=["-A", "app", "worker", "--pool", "threads", "-D"],
    # )
    # if isinstance(celery_aps, int):
    #     AppLogger.error("celery实例对象启动失败")
    # else:
    #     AppLogger.info("celery实例对象启动成功")

    uvicorn.run(
        "main:application",
        host=AppConfig.get("app", "host"),
        port=AppConfig.getint("app", "port"),
        reload=AppConfig.getboolean("app", "reload")
    )
